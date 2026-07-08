---
id: UDG@20.15.2@MMLCommand@LST HBUSRCTRL
type: MMLCommand
name: LST HBUSRCTRL（查询高带宽用户功能控制参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HBUSRCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级全局参数
- 高带宽用户功能控制参数
status: active
---

# LST HBUSRCTRL（查询高带宽用户功能控制参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询高带宽用户功能相关控制参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [高带宽用户功能控制参数（HBUSRCTRL）](configobject/UDG/20.15.2/HBUSRCTRL.md)

## 使用实例

查询高带宽用户功能相关控制参数：

```
%%LST HBUSRCTRL:;
```

```
%%
RETCODE = 0  操作成功

高带宽用户功能控制参数
----------------------
              高带宽用户快转加速开关  =  不使能
              高带宽用户资源均衡开关  =  不使能
                      全局协议组名称  =  NULL
    本地配置高带宽用户老化时间（秒）  =  60
订阅接口下发高带宽用户老化时间（秒）  =  300
      自学习高带宽用户老化时间（秒）  =  7200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询高带宽用户功能控制参数（LST-HBUSRCTRL）_42127243.md`
