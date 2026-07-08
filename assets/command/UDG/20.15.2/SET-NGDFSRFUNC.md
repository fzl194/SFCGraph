---
id: UDG@20.15.2@MMLCommand@SET NGDFSRFUNC
type: MMLCommand
name: SET NGDFSRFUNC（设置双发选收配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NGDFSRFUNC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 5G LAN双发选收功能配置
status: active
---

# SET NGDFSRFUNC（设置双发选收配置）

## 功能

**适用NF：UPF**

该命令用于设置指定5G LAN组的双发选收功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |
| DFSRSWITCH | 双发选收功能开关 | 可选必选说明：必选参数<br>参数含义：双发选收功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGDFSRFUNC]] · 双发选收配置（NGDFSRFUNC）

## 使用实例

开启双发选收开关：

```
SET NGDFSRFUNC: VNINSTANCE="a0000001-460-003-01", DFSRSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NGDFSRFUNC.md`
