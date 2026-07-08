---
id: UNC@20.15.2@MMLCommand@LST PNFALLOWDOMAIN
type: MMLCommand
name: LST PNFALLOWDOMAIN（查询对端NF允许的域名信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFALLOWDOMAIN
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
- 对端NF域名信息管理
status: active
---

# LST PNFALLOWDOMAIN（查询对端NF允许的域名信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询对端NF服务支持的允许访问的域名。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFALLOWDOMAIN]] · 对端NF允许的域名信息（PNFALLOWDOMAIN）

## 使用实例

查询对端NF支持的域名信息。

```
%%LST PNFALLOWDOMAIN:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = smf_instance_0
服务实例标识 = service_instance_0
      NF域名 = huawei.com
（结果个数 = 1）

---- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFALLOWDOMAIN.md`
