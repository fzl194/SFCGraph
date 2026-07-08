---
id: UNC@20.15.2@MMLCommand@LST NRFPARA
type: MMLCommand
name: LST NRFPARA（查询NRF协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- NRF配置参数管理
status: active
---

# LST NRFPARA（查询NRF协议参数）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于查询NRF协议相关的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPARA]] · NRF协议参数（NRFPARA）

## 使用实例

查询实例名称为NRF_Instance_0的NRF的参数相关的配置信息。

```
%%LST NRFPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
         NRF实例名称  =  NRF_Instance_0
            等待时长  =  5
        最大重传次数  =  3
            心跳时长  =  60
心跳是否携带Load信息  =  否
        订阅流程开关  =  OFF
      OAUTH2鉴权开关  =  OFF
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPARA.md`
