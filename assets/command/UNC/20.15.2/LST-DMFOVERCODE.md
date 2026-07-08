---
id: UNC@20.15.2@MMLCommand@LST DMFOVERCODE
type: MMLCommand
name: LST DMFOVERCODE（查询触发重选路由的错误码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMFOVERCODE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter协议接口重选路配置
status: active
---

# LST DMFOVERCODE（查询触发重选路由的错误码）

## 功能

**适用网元：SGSN、MME**

该命令用于查询触发重选路由的错误码。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMFOVERCODE]] · 触发重选路由的错误码（DMFOVERCODE）

## 使用实例

查询触发重选路由的错误码:

LST DMFOVERCODE;

```
%%LST DMFOVERCODE:;%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
  触发重选路由的错误码

  3002
  3004
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMFOVERCODE.md`
