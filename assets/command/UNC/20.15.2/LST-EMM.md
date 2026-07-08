---
id: UNC@20.15.2@MMLCommand@LST EMM
type: MMLCommand
name: LST EMM（查询S1模式MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EMM
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM协议参数管理
- S1模式MM协议参数
status: active
---

# LST EMM（查询S1模式MM协议参数）

## 功能

**适用网元：MME**

该命令用于查看4G移动性管理参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMM]] · S1模式MM协议参数（EMM）

## 使用实例

查询EMM（EPS Mobility Management）参数：

LST EMM:;

```
%%LST EMM:;%%
RETCODE = 0  操作成功。
操作结果如下
----------
                         T3422(s)  =  6
                     N3422(times)  =  4
                         T3450(s)  =  6
                     N3450(times)  =  4
                         T3460(s)  =  6
                     N3460(times)  =  4
                         T3470(s)  =  6
                     N3470(times)  =  4
                       T3412(min)  =  54
                       T3402(min)  =  12
                         T3413(s)  =  6
                     N3413(times)  =  2
              重寻呼间隔递增值(s)  =  0
           高优先级业务的T3413(s)  =  2
       高优先级业务的N3413(times)  =  4
高优先级业务的重寻呼间隔递增值(s)  =  0
              移动可达定时器(min)  =  58
    不可达用户隐式分离定时器(min)  =  0
              GUTI重分配定时器(h)  =  0
          Attach或TAU中重分配GUTI  =  重分配GUTI
            Handover准备定时器(s)  =  10
        源侧Handover完成定时器(s)  =  10
      目标侧Handover完成定时器(s)  =  10
                      T3定时器(s)  =  10
        测试用GUTI重分配定时器(m)  =  0
        切换流程资源释放定时器(s)  =  2
            GUTI重分配最大间隔(h)  =  0

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式MM协议参数(LST-EMM)_26305338.md`
