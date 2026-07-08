---
id: UNC@20.15.2@MMLCommand@CLR SMFCACHE
type: MMLCommand
name: CLR SMFCACHE（清除SMF缓存信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: SMFCACHE
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF缓存策略管理
status: active
---

# CLR SMFCACHE（清除SMF缓存信息）

## 功能

**适用NF：AMF**

该命令用于清除本地缓存的SMF与TAI列表映射关系以及PGW FQDN与锚点SMF映射关系。

如果输入INSTANCEID代表清除指定SMF与TAI的映射关系的缓存；如果不输入任何参数代表清除所有映射关系的缓存。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | SMF实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定待清除SMF与TAI映射关系所在的SMF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFCACHE]] · 缓存的SMF与TAI映射关系（SMFCACHE）

## 使用实例

清除本地所有缓存的映射关系，执行如下命令：

```
CLR SMFCACHE:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除SMF缓存信息（CLR-SMFCACHE）_35273617.md`
