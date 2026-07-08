---
id: UNC@20.15.2@MMLCommand@LST SBCFUNC
type: MMLCommand
name: LST SBCFUNC（查询小区广播功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBCFUNC
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBc参数
status: active
---

# LST SBCFUNC（查询小区广播功能）

## 功能

**适用网元：MME**

该命令用于查询小区广播功能参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [小区广播功能（SBCFUNC）](configobject/UNC/20.15.2/SBCFUNC.md)

## 使用实例

查询小区广播功能参数：

LST SBCFUNC:;

```
%%LST SBCFUNC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
           反馈功能开关  =  不支持
       上行消息流控开关  =  关闭
               流控阈值  =  10
Warning IND消息选路优化  =  关闭
    PWS IND消息选路优化  =  关闭
       大包处理功能开关  =  关闭
               离散时间  =  10
               基站个数  =  32
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询小区广播功能(LST-SBCFUNC)_72345979.md`
