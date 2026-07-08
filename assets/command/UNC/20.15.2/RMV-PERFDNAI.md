---
id: UNC@20.15.2@MMLCommand@RMV PERFDNAI
type: MMLCommand
name: RMV PERFDNAI（删除用于性能统计的数据网络访问标识信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFDNAI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFDNAI（删除用于性能统计的数据网络访问标识信息）

## 功能

**适用NF：SMF**

该命令用于删除可用于性能统计的数据网络访问标识信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用于性能统计的数据网络访问标识信息（PERFDNAI）](configobject/UNC/20.15.2/PERFDNAI.md)

## 使用实例

删除一条名称为“huawei.com”的数据网络访问标识信息，用于性能统计，执行如下命令：

```
RMV PERFDNAI: DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用于性能统计的数据网络访问标识信息（RMV-PERFDNAI）_16753890.md`
