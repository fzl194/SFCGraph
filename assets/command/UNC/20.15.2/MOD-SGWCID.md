---
id: UNC@20.15.2@MMLCommand@MOD SGWCID
type: MMLCommand
name: MOD SGWCID（修改SGW-C网络标识符）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGWCID
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- SGW-C信息管理
status: active
---

# MOD SGWCID（修改SGW-C网络标识符）

## 功能

**适用NF：SGW-C**

该命令用于修改SGW-C全球唯一标识的SGW-C标识信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成SGW-C的全球唯一标识的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成SGW-C的全球唯一标识的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| SGWCID | SGW-C标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成SGW-C的全球唯一标识的SGW-C标识信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCID]] · SGW-C网络标识符（SGWCID）

## 使用实例

当运营商需要修改SGW-C的全球唯一标识为123-45-00102时，执行命令如下：

```
MOD SGWCID:MCC="123",MNC="45",SGWCID="00102";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGW-C网络标识符（MOD-SGWCID）_36923529.md`
