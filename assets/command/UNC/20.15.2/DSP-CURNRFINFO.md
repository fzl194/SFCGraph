---
id: UNC@20.15.2@MMLCommand@DSP CURNRFINFO
type: MMLCommand
name: DSP CURNRFINFO（显示当前NRF实例信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CURNRFINFO
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
- CBCF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF配置管理
- NRF实例配置管理
status: active
---

# DSP CURNRFINFO（显示当前NRF实例信息）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBCF**

显示当前NF对接的NRF实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [当前NRF实例信息（CURNRFINFO）](configobject/UNC/20.15.2/CURNRFINFO.md)

## 使用实例

显示当前NF对接的NRF实例信息：

```
%%DSP CURNRFINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
      NRF实例ID  =  NRF_Instance_0
NRF绑定的NF类型  =  non-NRF
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示当前NRF实例信息（DSP-CURNRFINFO）_12701646.md`
