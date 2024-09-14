import matplotlib.pyplot as plt

def estimate_trend(y, d):
    n = len(y)
    trend = [0]*n
    for t in range(n):
        if d % 2 == 1:  # odd d
            sum_y = sum(y[max(0, t-d//2):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        else:  # even d
            sum_y = sum(y[max(0, t-d//2+1):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        trend[t] = sum_y / count
    return trend

def estimate_seasonality(y, d, trend):
    n = len(y)
    seasonality = [0]*n
    for t in range(n):
        seasonality[t] = y[t] / trend[t]
    return seasonality

# Example usage:
y = [28798,
56459,
62448,
49569,
30584,
18436,
14724,
11649,
10476,
11094,
15287,
16715,
31812,
60994,
64896,
58104,
27488,
14305,
11199,
8179,
9850,
9938,
13031,
15918,
29587,
54242,
49582,
45403,
29710,
15371,
12386,
9722,
9489,
9614,
13019,
13424,
27830,
43621,
57010,
]
 # Time series data
d = 3  # Number of seasons (odd)
# d = 4  # Number of seasons (even)

trend = estimate_trend(y, d)
seasonality = estimate_seasonality(y, d, trend)
# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(y, label='Original Time Series')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(trend, label='Trend Component')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(seasonality, label='Seasonality Component')
plt.legend()

plt.tight_layout()
plt.show()



