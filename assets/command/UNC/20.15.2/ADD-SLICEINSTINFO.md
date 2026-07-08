---
id: UNC@20.15.2@MMLCommand@ADD SLICEINSTINFO
type: MMLCommand
name: ADD SLICEINSTINFO（增加服务支持的切片实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SLICEINSTINFO
command_category: 配置类
applicable_nf:
- SMF
- AMF
- NRF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务支持的切片实例管理
status: active
---

# ADD SLICEINSTINFO（增加服务支持的切片实例）

## 功能

**适用NF：SMF、AMF、NRF、NSSF、NCG**

该命令用于增加一个切片实例管理。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIINFO | 网络分片实例信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络分片实例信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。本参数的构成字符只能是字母A～Z或a～z、数字0～9和中划线"-"，且不能以中划线“-”开头或结尾。<br>默认值：无<br>配置原则：无 |
| NSSIID | 网络分片子网实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络分片子网实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。本参数的构成字符只能是字母A～Z或a～z、数字0～9和中划线"-"，且不能以中划线“-”开头或结尾。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SLICEINSTINFO]] · 服务支持的切片实例（SLICEINSTINFO）

## 使用实例

增加NSIINFO为“NSSI-C-001-HDBNJ-NSSMF-01-A-HW”，NSSIID为“NSSI-C-001-HDBNJ-NSSMF-01-A-HW01”：

```
ADD SLICEINSTINFO:NSIINFO="NSSI-C-001-HDBNJ-NSSMF-01-A-HW",NSSIID="NSSI-C-001-HDBNJ-NSSMF-01-A-HW01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SLICEINSTINFO.md`
