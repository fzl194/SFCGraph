---
id: UNC@20.15.2@MMLCommand@LST PROXYSMFCTRL
type: MMLCommand
name: LST PROXYSMFCTRL（查询proxy SMF控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROXYSMFCTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SMFS8管理
status: active
---

# LST PROXYSMFCTRL（查询proxy SMF控制）

## 功能

**适用NF：SMF**

该命令用于查询PROXYSMFCTRL。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于配置移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定控制类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的DNN名称需要符合DNN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROXYSMFCTRL]] · proxy SMF控制（PROXYSMFCTRL）

## 使用实例

查询MCC为“460”、MNC为“00”、控制类型为整系统级别的proxy SMF控制配置。

```
%%LST PROXYSMFCTRL:MCC="460",MNC="00",CTRLTYPE=GLOBAL_LEVEL;%%
RETCODE = 0 操作成功
结果如下
--------
                     移动国家码 = 460
                       移动网号 =  00
                       控制类型 = 整系统级别
                           DNN = NULL
                  Proxy QoS来源 = V-SMF
                    TAC转换策略 = 默认策略
                           TAC = NULL
E-UTRAN Cell Identifier转换策略 = 默认策略
       E-UTRAN Cell Identifier = NULL
                       解析方式 = 本地配置优先
                   支持的IP类型 = IPV4V6
         语音业务回归属地功能开关 = 关闭
                     互操作开关 = 关闭
                  归属地接口模式 = 与左侧联动
         数据业务回归属地功能开关 = 关闭
                             DNN格式 = 仅携带NI
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询proxy-SMF控制（LST-PROXYSMFCTRL）_91923233.md`
