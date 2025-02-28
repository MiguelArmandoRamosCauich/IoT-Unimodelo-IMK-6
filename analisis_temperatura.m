% Leer temperatura de un canal ThingSpeak y calcular el promedio de cada grupo de 10 datos.
% Mostrar una alerta si alguno de los promedios supera los 35°C.

% ID del canal de lectura
readChannelID = 2841576; 
% ID del campo de temperatura
temperatureFieldID = 1; 
% Clave API de lectura (si es necesario)
readAPIKey = 'PK0JEWLFACZLHQUE'; 

% Obtener los últimos 100 valores de temperatura
numData = 1457; % Ajusta según la cantidad de datos disponibles
temperature = thingSpeakRead(readChannelID, 'Fields', temperatureFieldID, ...
    'NumPoints', numData, 'ReadKey', readAPIKey); 

% Verificar si se obtuvieron datos suficientes
if isempty(temperature) || length(temperature) < 10
    disp('Error: No se pudieron obtener suficientes datos de ThingSpeak.');
    return;
end

% Número de grupos de 10 datos
numGroups = floor(length(temperature) / 10);

% Inicializar vector para almacenar los promedios
avgTemperatures = zeros(1, numGroups);

% Calcular promedios por cada 10 datos
for i = 1:numGroups
    startIdx = (i - 1) * 10 + 1;
    endIdx = startIdx + 9;
    avgTemperatures(i) = mean(temperature(startIdx:endIdx));
    
    % Mostrar el promedio calculado
    disp(['Promedio del grupo ', num2str(i), ': ', num2str(avgTemperatures(i)), '°C']);
    
    % Mostrar alerta si el promedio supera los 35°C
    if avgTemperatures(i) > 35
        disp(['¡ALERTA! El promedio del grupo ', num2str(i), ' supera los 35°C.']);
    end
end
