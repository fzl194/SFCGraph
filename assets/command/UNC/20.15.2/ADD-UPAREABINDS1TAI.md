---
id: UNC@20.15.2@MMLCommand@ADD UPAREABINDS1TAI
type: MMLCommand
name: ADD UPAREABINDS1TAI（增加UPF服务区名称绑定的4G TAI范围）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPAREABINDS1TAI
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- TAI绑定UP区域
status: active
---

# ADD UPAREABINDS1TAI（增加UPF服务区名称绑定的4G TAI范围）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于增加UPF服务区名称绑定的4G TAI范围。

## 注意事项

- 该命令执行后立即生效。

- 通过ADD UPAREABINDS1TAI/ADD SUFFIXS1TAIAREA配置的各UPF服务区名称绑定的4G TAI范围不允许出现交集。

- 最多可输入16384条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为S1TAI。 |
| S1BEGINTAI | UPF服务区名称绑定4G TAI范围起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定4G TAI范围起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。后4位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |
| S1ENDTAI | UPF服务区名称绑定4G TAI范围结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定4G TAI范围结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。后4位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPAREABINDS1TAI]] · UPF服务区名称绑定的4G TAI范围（UPAREABINDS1TAI）

## 使用实例

增加UPF服务区名称为“UPAREA1”的4G TAI绑定范围123010001~123011111：

```
ADD UPAREABINDS1TAI: AREANAME="UPAREA1", S1BEGINTAI="123010001", S1ENDTAI="123011111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UPAREABINDS1TAI.md`
