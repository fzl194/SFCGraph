---
id: UNC@20.15.2@MMLCommand@RMV NGTALISTPAGINGCFG
type: MMLCommand
name: RMV NGTALISTPAGINGCFG（删除N2模式TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGTALISTPAGINGCFG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG TALIST寻呼管理
status: active
---

# RMV NGTALISTPAGINGCFG（删除N2模式TALIST寻呼不重发TAC区间）

## 功能

**适用NF：AMF**

该命令用于删除N2模式TALIST寻呼不重发TAC区间。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| TACSTART | 跟踪区域起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域起始编码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：<br>本参数由6位十六进制数组成，不区分大小写。MCC、MNC相同时，不同记录的TAC区间不能有交集。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTALISTPAGINGCFG]] · N2模式TALIST寻呼不重发TAC区间（NGTALISTPAGINGCFG）

## 使用实例

删除TAC起始为11BF85的跟踪区间，执行如下命令：

```
RMV NGTALISTPAGINGCFG: MCC="123", MNC="45",TACSTART="11BF85";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGTALISTPAGINGCFG.md`
