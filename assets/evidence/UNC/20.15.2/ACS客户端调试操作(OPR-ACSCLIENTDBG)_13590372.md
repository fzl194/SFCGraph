# ACS客户端调试操作(OPR ACSCLIENTDBG)

- [命令功能](#ZH-CN_MMLREF_0000002113590372__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002113590372__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002113590372__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0000002113590372__1.3.4)
- [输出结果说明](#ZH-CN_MMLREF_0000002113590372__1.3.5)
- [参考信息](#ZH-CN_MMLREF_0000002113590372__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002113590372)

该命令用于向ACS配置客户端发送调试操作。

## [注意事项](#ZH-CN_MMLREF_0000002113590372)

无。

## [参数说明](#ZH-CN_MMLREF_0000002113590372)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEBUGTYPE | 调试类型 | 可选必选说明：必选参数。<br>参数含义：用于指定需要调试操作的类型。<br>取值范围：枚举类型。<br>- saveNextSyncdata(保存下次对账文件)：保存客户端下次对账的配置文件。<br>- saveDb(保存客户端数据库)：保存客户端侧DB文件。<br>默认值：无。<br>配置原则：无。 |
| DEBUGVALUE | 调试内容 | 可选必选说明：可选参数。<br>参数含义：<br>自定义调试操作内容。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |
| SERVICENAME | 服务名称 | 可选必选说明：条件必选参数，该参数在<br>“DEBUGTYPE”<br>配置为<br>“saveNextSyncdata”<br>或<br>“saveDb”<br>时为必选参数。<br>参数含义：用于指定需要执行调试操作的微服务名称。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |
| INSTANCEID | 实例ID | 可选必选说明：条件必选参数，该参数在<br>“DEBUGTYPE”<br>配置为<br>“saveNextSyncdata”<br>或<br>“saveDb”<br>时为必选参数。<br>参数含义：用于指定需要执行调试操作的微服务实例ID。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |

## [使用实例](#ZH-CN_MMLREF_0000002113590372)

向ACS配置客户端发送保存下次对账文件调试操作时，执行以下命令：

```
OPR ACSCLIENTDBG: DEBUGTYPE=saveNextSyncdata, SERVICENAME="101", INSTANCEID="hafetcd-pod12-0__104__0";
```

```
%%OPR ACSCLIENTDBG: DEBUGTYPE=saveNextSyncdata, SERVICENAME="101", INSTANCEID="hafetcd-pod12-0__104__0";%% 
RETCODE = 0  操作成功  

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000002113590372)

该命令执行正常，会返回命令执行成功的提示信息。

命令执行异常，请联系华为技术支持处理。常见异常场景如 [表1 错误码列表](删除配置对象告警阈值(RMV CFGTHRESHOLD)_72490293.md#ZH-CN_MMLREF_0000002072490293__table10552443815) 所示。

*表1 错误码列表*

| 错误码 | 错误码解释 | 原因分析 | 处理建议 |
| --- | --- | --- | --- |
| 4790 | 操作异常。 | ACS内部错误，如内部服务异常等。 | 请联系<br>华为<br>技术支持。 |

## [参考信息](#ZH-CN_MMLREF_0000002113590372)

无。
