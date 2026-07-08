---
id: UNC@20.15.2@MMLCommand@LST NFMGMTTIMER
type: MMLCommand
name: LST NFMGMTTIMER（查询NF管理模块的定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFMGMTTIMER
command_category: 查询类
applicable_nf:
- NRF
- SMF
- AMF
- NSSF
- NCG
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF定时器管理
status: active
---

# LST NFMGMTTIMER（查询NF管理模块的定时器配置）

## 功能

**适用NF：NRF、SMF、AMF、NSSF、NCG、SMSF**

该命令用于查询NF管理模块的定时器配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF管理模块的定时器配置（NFMGMTTIMER）](configobject/UNC/20.15.2/NFMGMTTIMER.md)

## 使用实例

运营商A需要查询NF管理模块的定时器配置。

```
%%LST NFMGMTTIMER:;%%
RETCODE = 0  操作成功

结果如下
--------
URI地址表老化周期  =  168
URI地址表刷新间隔  =  10
URI地址表扫描间隔  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF管理模块的定时器配置（LST-NFMGMTTIMER）_01006689.md`
