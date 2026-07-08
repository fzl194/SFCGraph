---
id: UNC@20.15.2@MMLCommand@LST PMM
type: MMLCommand
name: LST PMM（查询Iu模式MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PMM
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
- 移动性管理
- MM协议参数管理
- Iu模式MM协议参数
status: active
---

# LST PMM（查询Iu模式MM协议参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查看PMM（3G移动性管理功能）定时器参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PMM]] · Iu模式MM协议参数（PMM）

## 使用实例

查询PMM参数：

LST PMM:;

```
%%LST PMM:;%%
RETCODE = 0  操作成功。

PMM参数表
---------
                     T3322(s)  =  6
                 N3322(times)  =  4
                     T3350(s)  =  6
                 N3350(times)  =  4
                     T3360(s)  =  6
                 N3360(times)  =  4
                     T3370(s)  =  6
                 N3370(times)  =  4
                     T3313(s)  =  6
                 N3313(times)  =  2
             T3302定时器（s）  =  4
          重寻呼间隔递增值(s)  =  0
      周期路由更新定时器(min)  =  54
            MS可达定时器(min)  =  58
                     保留参数  =  0
      重定位资源分配定时器(s)  =  10
      旧侧重定位完成定时器(s)  =  10
      新侧重定位完成定时器(s)  =  10
                  T3定时器(s)  =  10
  释放非活动Iu连接定时器(min)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式MM协议参数(LST-PMM)_72345123.md`
