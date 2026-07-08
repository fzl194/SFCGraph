---
id: UNC@20.15.2@MMLCommand@DSP SDRSROUTE
type: MMLCommand
name: DSP SDRSROUTE（显示SDRS中的APPROUTEINFO信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRSROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRSROUTE（显示SDRS中的APPROUTEINFO信息）

## 功能

该命令用于查询SDRS中指定APP的ROUTE策略信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | app类型 | 可选必选说明：必选参数<br>参数含义：该参数标识下发APP路由策略的APP类型，可以使用<br>[**DSP SDRSAPPTYPE**](显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)<br>命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CELLID | Cell ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SDR调试消息发送的CELLID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDRSROUTE]] · SDRS中的APPROUTEINFO信息（SDRSROUTE）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRSROUTE.md`
