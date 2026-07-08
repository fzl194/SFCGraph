---
id: UNC@20.15.2@MMLCommand@LST PFRES
type: MMLCommand
name: LST PFRES（查询带宽资源管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFRES
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- 带宽资源管理
- 带宽资源参数管理
status: active
---

# LST PFRES（查询带宽资源管理参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询用户面资源管理信息参数，这些值都是通过 [**SET PFRES**](设置带宽资源管理参数(SET PFRES)_26305658.md) 设置的。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFRES]] · 带宽资源使用明细（PFRES）

## 使用实例

查询用户面资源管理信息参数：

LST PFRES:;

```
%%LST PFRES:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
         转发带宽过载门限(%)  =  75
     转发带宽过载恢复门限(%)  =  70
         转发带宽拥塞门限(%)  =  90
     转发带宽拥塞恢复门限(%)  =  85
2G用户流量上报门限值(kbytes)  =  1000
3G用户流量上报门限值(kbytes)  =  1000
              CPU过载门限(%)  =  75
          CPU过载恢复门限(%)  =  65
              CPU拥塞门限(%)  =  95
          CPU拥塞恢复门限(%)  =  85
       包转发速率过载门限(%)  =  90
   包转发速率过载恢复门限(%)  =  87
       包转发速率拥塞门限(%)  =  97
   包转发速率拥塞恢复门限(%)  =  93

         (结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询带宽资源管理参数(LST-PFRES)_72345449.md`
