---
id: UNC@20.15.2@MMLCommand@LST GWOFFLOADPARA
type: MMLCommand
name: LST GWOFFLOADPARA（查询网关迁移参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWOFFLOADPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# LST GWOFFLOADPARA（查询网关迁移参数）

## 功能

**适用网元：MME**

该命令用于查询S-GW或P-GW故障场景下，对用户业务进行迁移的控制参数，包含迁移任务的启动时延、迁移速率以及S11/S5接口故障迁移控制开关。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWOFFLOADPARA]] · 网关迁移参数（GWOFFLOADPARA）

## 使用实例

查询设置的故障迁移参数：

LST GWOFFLOADPARA:;

```
%%LST GWOFFLOADPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 迁移时延（分钟）  =  3
迁移速率（个/秒）  =  200
 接口故障迁移开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网关迁移参数（LST-GWOFFLOADPARA）_26146082.md`
