---
id: UNC@20.15.2@MMLCommand@LST HTR
type: MMLCommand
name: LST HTR（查询HTR功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- Gr HTR流控局向管理
- 流控功能管理
status: active
---

# LST HTR（查询HTR功能）

## 功能

**适用网元：SGSN**

该命令用于查询HTR（Hard to Reach）流控功能的相关参数。当Gr或者Ge口出现拥塞时需要进行流控。

Gr口拥塞的表现和控制场景：

- 场景1：SGSN与HLR之间直连链路拥塞，此时进行自动启控。
- 场景2：HLR过载，此时进行手工启控。
- 场景3：STP到HLR链路拥塞，此时进行手工启控。
- 场景4：STP过载，此时进行手工启控。
- 场景5：SGSN与STP之间直连链路拥塞，此时进行自动启控。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [HTR功能（HTR）](configobject/UNC/20.15.2/HTR.md)

## 使用实例

查询HTR参数：

LST HTR:;

```
%%LST HTR:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
         HTR功能开关  =  是
     HTR功能手工开关  =  否
        流控目标时延  =  1500
 HTR配置局向是否生效  =  否
     HTR流控启动阈值  =  50
     HTR流控恢复阈值  =  80
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTR功能(LST-HTR)_26146150.md`
