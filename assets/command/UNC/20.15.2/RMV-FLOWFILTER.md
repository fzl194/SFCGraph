---
id: UNC@20.15.2@MMLCommand@RMV FLOWFILTER
type: MMLCommand
name: RMV FLOWFILTER（删除流过滤器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: FLOWFILTER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务过滤器
- 流过滤器
status: active
---

# RMV FLOWFILTER（删除流过滤器）

## 功能

**适用NF：PGW-C、SMF**

![](删除流过滤器（RMV FLOWFILTER）_09897154.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入流过滤器名称，表示删除系统内的所有流过滤器。删除后UL CL场景及ADC场景下使用该流过滤器的用户可能会因为无法命中流过滤器导致相关业务受损，请谨慎使用并联系华为支持协助操作。

该命令删除所有的流过滤器，或者删除指定名称的流过滤器。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入任何参数，表示要删除所有的流过滤器。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置“流过滤器名称”， 该参数可供RULE命令中的“流过滤器名称”参数引用。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数填写时删除系统中的一个过滤器，不填时删除系统中的所有过滤器。 |

## 操作的配置对象

- [流过滤器（FLOWFILTER）](configobject/UNC/20.15.2/FLOWFILTER.md)

## 使用实例

删除流过滤器：“FlowFilterName”为“testflowfiltername”：

```
RMV FLOWFILTER:FLOWFILTERNAME="testflowfiltername";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除流过滤器（RMV-FLOWFILTER）_09897154.md`
