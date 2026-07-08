---
id: UNC@20.15.2@MMLCommand@LST SIGSUPPRESS
type: MMLCommand
name: LST SIGSUPPRESS（查询S11接口信令风暴抑制功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SIGSUPPRESS
command_category: 查询类
applicable_nf:
- MME
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
- 信令抑制管理
- S11接口故障场景信令抑制管理
status: active
---

# LST SIGSUPPRESS（查询S11接口信令风暴抑制功能参数）

## 功能

**适用网元：MME**

该命令用于查询S11接口信令风暴抑制功能的相关参数的配置。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SIGSUPPRESS]] · S11接口信令风暴抑制功能的控制与统计信息（SIGSUPPRESS）

## 使用实例

查询S11接口信令风暴抑制功能参数：

LST SIGSUPPRESS:;

```
%%LST SIGSUPPRESS:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 S11接口信令抑制开关  =  关闭
    信令抑制配置策略  =  系统缺省值
抑制用户数控制参考值  =  500000
      抑制时长（分）  =  15
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SIGSUPPRESS.md`
