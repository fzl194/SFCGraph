---
id: UNC@20.15.2@MMLCommand@RMV ALLOWEDNFDOMAIN
type: MMLCommand
name: RMV ALLOWEDNFDOMAIN（删除NF或NF服务支持的域名）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALLOWEDNFDOMAIN
command_category: 配置类
applicable_nf:
- AMF
- SMF
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
- 服务支持的域名配置管理
status: active
---

# RMV ALLOWEDNFDOMAIN（删除NF或NF服务支持的域名）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于删除NF或NF服务实例支持的域名。当NF或NF服务实例不再支持为某个域名服务时，需要对域名进行删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定索引标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDNFDOMAIN]] · NF或NF服务支持的域名（ALLOWEDNFDOMAIN）

## 使用实例

运营商A需要删除索引标识为0的域名支持信息。

```
RMV ALLOWEDNFDOMAIN: INDEX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF或NF服务支持的域名（RMV-ALLOWEDNFDOMAIN）_09651481.md`
