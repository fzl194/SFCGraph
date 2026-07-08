---
id: UNC@20.15.2@MMLCommand@ADD UPAREA
type: MMLCommand
name: ADD UPAREA（增加UPF服务区）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPAREA
command_category: 配置类
applicable_nf:
- SMF
- GGSN
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
- UP区域管理
status: active
---

# ADD UPAREA（增加UPF服务区）

## 功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于增加UPF服务区域，并指定服务区域的名称与类型。后续指定UPF支持的服务范围时需要以本配置中的服务区域为粒度进行分配。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入49152条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置UPF服务区的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与LST PNFSMFSERAREA查询结果中的SMFSERVINGAREA保持一致。 |
| AREATYPE | UPF服务区类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置UPF服务区的类型。<br>数据来源：全网规划<br>取值范围：<br>- S1TAI（4G类型的TAI）<br>- N2TAI（5G类型的TAI）<br>- LAI（23G类型的LAI）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF服务区（UPAREA）](configobject/UNC/20.15.2/UPAREA.md)

## 使用实例

增加4G类型的UPF服务区：

```
ADD UPAREA: AREANAME="UPAREA1", AREATYPE=S1TAI;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF服务区（ADD-UPAREA）_09652457.md`
