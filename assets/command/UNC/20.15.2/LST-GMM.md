---
id: UNC@20.15.2@MMLCommand@LST GMM
type: MMLCommand
name: LST GMM（查询Gb模式MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM协议参数管理
- Gb模式MM协议参数
status: active
---

# LST GMM（查询Gb模式MM协议参数）

## 功能

**适用网元：SGSN**

该命令用于查询GMM(2G移动性管理)定时器及其他参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMM]] · Gb模式MM协议参数（GMM）

## 使用实例

查询GMM参数：

LST GMM:;

```
%%LST GMM:;%%
RETCODE = 0  执行成功。

操作结果如下
--------------
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
               T3302 timer(s)  =  4
          重寻呼间隔递增值(s)  =  0
                准备定时器(s)  =  44
      周期路由更新定时器(min)  =  54
            MS可达定时器(min)  =  58
                    保留参数1  =  0
                  T3定时器(s)  =  10
                      缺省QoS  =  
0B9211

                       优先级  =  0
                    保留参数2  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Gb模式MM协议参数(LST-GMM)_26145524.md`
