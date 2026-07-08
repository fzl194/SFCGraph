---
id: UNC@20.15.2@MMLCommand@LST LOADCHECKINFO
type: MMLCommand
name: LST LOADCHECKINFO（查询CSLB负载不均衡检测功能的参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOADCHECKINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- 工程调测
- 5G工程命令
status: active
---

# LST LOADCHECKINFO（查询CSLB负载不均衡检测功能的参数）

## 功能

该命令用于查询CSLB负载不均衡检测功能的参数。

## 注意事项

此功能仅在UPF中使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [CSLB负载不均衡检测功能的参数（LOADCHECKINFO）](configobject/UNC/20.15.2/LOADCHECKINFO.md)

## 使用实例

查询当前CSLB负载不均衡检测功能的参数。

```
%%LST LOADCHECKINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
CSLB负载不均衡检测开关  =  开启
       CPU基础阈值 (%)  =  50
       CPU阈值上限 (%)  =  50
       CPU阈值下限 (%)  =  30
    收包数阈值上限 (%)  =  80
    收包数阈值下限 (%)  =  40
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSLB负载不均衡检测功能的参数（LST-LOADCHECKINFO）_97964757.md`
