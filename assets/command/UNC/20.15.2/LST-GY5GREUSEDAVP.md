---
id: UNC@20.15.2@MMLCommand@LST GY5GREUSEDAVP
type: MMLCommand
name: LST GY5GREUSEDAVP（查询5G用户接入时，Gy接口重用字段的填写方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GY5GREUSEDAVP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单字段控制
- 5G用户话单重用字段控制
status: active
---

# LST GY5GREUSEDAVP（查询5G用户接入时，Gy接口重用字段的填写方式）

## 功能

**适用NF：SMF、PGW-C**

查询5G用户接入时，Gy接口重用字段的填写方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GY5GREUSEDAVP]] · 5G用户接入时，Gy接口重用字段的填写方式（GY5GREUSEDAVP）

## 使用实例

查询5G用户接入时，Gy接口重用字段的填写方式。

```
%%LST GY5GREUSEDAVP:;%%
RETCODE = 0  操作成功

结果如下
--------
      无线接入技术  =  携带固定用户信息
      用户位置信息  =  携带真实用户信息
用户位置信息固定值  =  8212f470ffff12f470ffffffff
               QoS  =  携带R8的QoS信息
         QoS固定值  =  08-4807001e848000195460
      服务节点类型  =  携带真实用户信息
             NSAPI  =  携带真实用户信息
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G用户接入时，Gy接口重用字段的填写方式（LST-GY5GREUSEDAVP）_52070868.md`
