---
id: UNC@20.15.2@MMLCommand@LST DMFUNC
type: MMLCommand
name: LST DMFUNC（查询Diameter配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMFUNC
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
- 信令传输管理
- Diameter管理
- Diameter参数
status: active
---

# LST DMFUNC（查询Diameter配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询diameter全局参数。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMFUNC]] · Diameter配置（DMFUNC）

## 使用实例

查询Diameter配置，运行如下命令:

**LST DMFUNC:;**

```

%%LST DMFUNC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
             重连方式  =  恒定时长
        重连定时器(s)  =  30
    等待回复定时器(s)  =  14
      看门狗定时器(s)  =  15
  连接侦测次数(times)  =  3
           消息版本号  =  1
等待对端响应定时器(s)  =  13
     重选路由功能开关  =  否
 心跳消息故障检测开关  =  关闭
         连接恢复次数  =  NULL
   连接恢复定时器(ms)  =  NULL
对端拥塞避免定时器(s)  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter配置(LST-DMFUNC)_26306082.md`
