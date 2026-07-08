---
id: UNC@20.15.2@MMLCommand@LST KPIMONPARA
type: MMLCommand
name: LST KPIMONPARA（查询KPI监控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: KPIMONPARA
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
- 操作维护
- 性能管理
- KPI监控
status: active
---

# LST KPIMONPARA（查询KPI监控参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询KPI监控功能的参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@KPIMONPARA]] · KPI监控参数（KPIMONPARA）

## 使用实例

查询KPI监控功能的参数：

LST KPIMONPARA:;

```
%%LST KPIMONPARA:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
 监控粒度=单进程
  监控开关= 打开  
关闭类型 =NULL 
关闭时长(分)= NULL   
告警开关=打开  
告警间隔周期（分）=60  
告警次数=3  
自愈开关=打开                               
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-KPIMONPARA.md`
