---
id: UNC@20.15.2@MMLCommand@LST INTERMMEFIXFC
type: MMLCommand
name: LST INTERMMEFIXFC（查询Inter-MME接入固定速率流控功能相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTERMMEFIXFC
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Inter-MME接入流控管理
status: active
---

# LST INTERMMEFIXFC（查询Inter-MME接入固定速率流控功能相关参数）

## 功能

**适用网元：MME**

该命令用于查询Inter-MME接入固定速率流控功能的相关参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/INTERMMEFIXFC]] · Inter-MME接入固定速率流控功能相关参数（INTERMMEFIXFC）

## 使用实例

查询Inter-MME接入固定速率流控功能的相关参数：

```
LST INTERMMEFIXFC:;
```

```
查询结果如下
-------------------------
                      流控粒度   =  单进程
         Attach接入流控功能开关  =  关闭
 Attach Request流控阈值作用范围  =  单进程
  Attach Request速率门限(个/秒)  =  4080
             SR接入流控功能开关  =  关闭
Service Request流控阈值作用范围  =  单进程
 Service Request速率门限(个/秒)  =  4080
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Inter-MME接入固定速率流控功能相关参数(LST-INTERMMEFIXFC)_57365241.md`
