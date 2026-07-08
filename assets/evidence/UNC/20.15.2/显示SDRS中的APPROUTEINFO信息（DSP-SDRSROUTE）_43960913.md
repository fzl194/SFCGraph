# 显示SDRS中的APPROUTEINFO信息（DSP SDRSROUTE）

- [命令功能](#ZH-CN_MMLREF_0000001143960913__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001143960913__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001143960913__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001143960913__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001143960913__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001143960913)

该命令用于查询SDRS中指定APP的ROUTE策略信息。

## [注意事项](#ZH-CN_MMLREF_0000001143960913)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001143960913)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001143960913)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | app类型 | 可选必选说明：必选参数<br>参数含义：该参数标识下发APP路由策略的APP类型，可以使用<br>[**DSP SDRSAPPTYPE**](显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)<br>命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CELLID | Cell ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SDR调试消息发送的CELLID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001143960913)

使用如下命令查询SDRS中缓存的ROUTE策略信息：

```
%%DSP SDRSROUTE: APPTYPE=114, CELLID="vup-pod-010-104-1-24__103__0";%%
RETCODE = 0  操作成功
结果如下
--------
          app类型 = 114
          Cell ID = vup-pod-010-104-1-24__103__0
发送的topicId列表 = 4217 4219 4211 32785
接收的topicId列表 = 4218 4220 32784
         路由算法 = 
[0/1] keyType[2] algoType[2 ATOM_ALGO_KEY_MATCH] algoOutputType[2 ATOM_ALGO_OUTPUT_MULTI_INSTANCE] instTeamFrom[0 ] appType[114] groupId[0] tableId[0x0]
(结果个数 = 1)
---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001143960913)

| 输出项名称 | 输出项解释 |
| --- | --- |
| app类型 | 该参数标识下发APP路由策略的APP类型，可以使用<br>[**DSP SDRSAPPTYPE**](显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)<br>命令获取。 |
| Cell ID | 该参数用于指定SDR调试消息发送的CELLID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。 |
| 发送的topicId列表 | 该参数用于表示业务app将要发送的topic id。 |
| 接收的topicId列表 | 该参数用于表示业务app将要接收到的topic id。 |
| 路由算法 | 该参数用于表示APPROUTE策略的路由算法。 |
