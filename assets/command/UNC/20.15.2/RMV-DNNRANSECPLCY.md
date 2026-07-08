---
id: UNC@20.15.2@MMLCommand@RMV DNNRANSECPLCY
type: MMLCommand
name: RMV DNNRANSECPLCY（删除DNN RAN侧安全策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNNRANSECPLCY
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC用户面安全策略管理
status: active
---

# RMV DNNRANSECPLCY（删除DNN RAN侧安全策略）

## 功能

**适用NF：SMF**

该命令用来删除基于DNN的RAN侧用户面安全策略。策略用于明确是否需要对RAN侧用户面进行完整性保护和加密保护。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当根据DNN、SST和SD能查询到本配置时，使用本配置的策略，否则使用SET RANSECPLCY中的策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络切片索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>本参数通过ADD PLMNNS命令进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNRANSECPLCY]] · DNN RAN侧安全策略（DNNRANSECPLCY）

## 使用实例

删除基于DNN的RAN侧用户面安全策略，执行如下命令：

```
RMV DNNRANSECPLCY:DNN="huawei.com", NSIDX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNNRANSECPLCY.md`
