

CREATE VIEW dbo.vw_SiteBirdObservers_LEFTJOIN

AS

SELECT B.ParkUnit, B.Plot, B.EventID, B.EventDateTime, O.ContactName AS ObserverInitials, B.Temperature_C, B.WindSpeed, B.WindDesc, B.Rain,
  B.PercentCloud, B.Noise, B.NoiseSummary, B.Interval, B.ObservationNumber, B.ScientificName, B.CommonName,
  B.Distance, DetectionType, B.Sex, B.Age, B.FlockSize, B.IsPreviousPlot, B.IsFlyOver, B.Comments


FROM dbo.vw_SitesBirds3 AS B

LEFT JOIN dbo.vw_BirdObservers AS O
  ON B.BirdSamplingEventID = O.BirdSamplingEventID

