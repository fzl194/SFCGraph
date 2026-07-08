---
id: UNC@20.15.2@MMLCommand@LST PNFNSILST
type: MMLCommand
name: LST PNFNSILST（查询对端NF实例网络切片标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFNSILST
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例网络切片标识管理
status: active
---

# LST PNFNSILST（查询对端NF实例网络切片标识）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置的对端NF实例支持的NSI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFNSILST]] · 对端NF实例网络切片标识（PNFNSILST）

## 使用实例

查询本地配置的对端NF支持的NSI信息。

```
%%LST PNFNSILST:;%%
RETCODE = 0 操作成功

结果如下
------------------------
    NF实例标识 = smf_instance_0
NF切片实例标识 = 10001
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端NF实例网络切片标识（LST-PNFNSILST）_09652554.md`
