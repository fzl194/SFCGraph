---
id: UNC@20.15.2@MMLCommand@LST NSSFFUNCSWITCH
type: MMLCommand
name: LST NSSFFUNCSWITCH（查询NSSF功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFFUNCSWITCH
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能开关配置
status: active
---

# LST NSSFFUNCSWITCH（查询NSSF功能开关）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF功能开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCSWITCH]] · NSSF功能开关（NSSFFUNCSWITCH）

## 使用实例

当运营商希望查询NSSF的各项功能的开启状态时，可以通过此命令查询：

```
%%LST NSSFFUNCSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
  按签约分配Configured切片开关  =  关闭
切片选择请求合法性判断增强开关  =  打开
      切片选择匹配策略增强开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NSSF功能开关（LST-NSSFFUNCSWITCH）_96242339.md`
