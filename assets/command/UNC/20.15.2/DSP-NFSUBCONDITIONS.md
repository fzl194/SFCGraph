---
id: UNC@20.15.2@MMLCommand@DSP NFSUBCONDITIONS
type: MMLCommand
name: DSP NFSUBCONDITIONS（查询NF订阅信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NFSUBCONDITIONS
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
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
- NRF管理
- NRF参数管理
- 注册与订阅管理
status: active
---

# DSP NFSUBCONDITIONS（查询NF订阅信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于查询当前NF的所有订阅信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSUBCONDITIONS]] · NF订阅信息（NFSUBCONDITIONS）

## 使用实例

查询当前NF的所有订阅信息。

```
%%DSP NFSUBCONDITIONS:;%%
RETCODE = 0  操作成功

结果如下
--------
      订阅标识  =  SubscribeId_1
      订阅条件  =  {Sst:460, Sd:AA}
  通知事件类型  =  {1}
       位置信息 = 10.107.240.216:81/SubSnssaiLocation
      失败次数  =  0
下次重订阅时间  = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NFSUBCONDITIONS.md`
