---
id: UNC@20.15.2@MMLCommand@LST HLRBYPASS
type: MMLCommand
name: LST HLRBYPASS（查询HLR故障Bypass功能控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HLRBYPASS
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HLR故障BYPASS功能
status: active
---

# LST HLRBYPASS（查询HLR故障Bypass功能控制参数）

## 功能

**适用网元：SGSN**

该命令用于查询HLR故障Bypass功能控制参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HLRBYPASS]] · HLR故障Bypass功能控制参数（HLRBYPASS）

## 使用实例

查询HLR故障Bypass功能控制参数信息：

```
LST HLRBYPASS:;
```

```
查询结果如下
-------------------------
    HLR Bypass功能开关  =  开启
退出Bypass状态恢复动作  =  优雅分离
 整系统扫描速率(个/秒)  =  100
      扫描时间间隔(秒)  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HLR故障Bypass功能控制参数(LST-HLRBYPASS)_04432482.md`
