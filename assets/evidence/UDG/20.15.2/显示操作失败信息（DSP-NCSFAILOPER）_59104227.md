# 显示操作失败信息（DSP NCSFAILOPER）

- [命令功能](#ZH-CN_CONCEPT_0259104227__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259104227__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259104227__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259104227__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259104227__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259104227__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259104227)

该命令用于显示操作失败信息。

#### [注意事项](#ZH-CN_CONCEPT_0259104227)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0259104227)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259104227)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BOARDTYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主OMU。<br>- slave：备OMU。<br>默认值：master |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259104227)

显示操作失败信息：

```
DSP NCSFAILOPER:BOARDTYPE=master
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
NETCONF会话ID  =  64
       时间戳  =  2016-08-04, 10:43:22:451
     错误信息  =  Invalid RPC request.;Oper=unknown;MsgId=.
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259104227)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NETCONF会话ID | NETCONF会话的标识。 |
| 时间戳 | 失败操作发生的时间。 |
| 错误信息 | 失败操作的详细信息。 |
