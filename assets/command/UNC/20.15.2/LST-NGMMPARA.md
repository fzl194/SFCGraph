---
id: UNC@20.15.2@MMLCommand@LST NGMMPARA
type: MMLCommand
name: LST NGMMPARA（查询5G MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMMPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动管理定时器
status: active
---

# LST NGMMPARA（查询5G MM协议参数）

## 功能

**适用NF：AMF**

该命令用于查看5G模式性移动性管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMMPARA]] · 5G MM协议参数（NGMMPARA）

## 使用实例

查询5G MM参数，执行如下命令：

```
%%LST NGMMPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                          T3522(s)  =  6
                      N3522(times)  =  4
                          T3550(s)  =  6
                      N3550(times)  =  4
                          T3560(s)  =  6
                      N3560(times)  =  4
                          T3570(s)  =  6
                      N3570(times)  =  4
                        T3512(min)  =  54
                        T3502(min)  =  12
                          T3513(s)  =  6
                      N3513(times)  =  2
                          T3555(s)  =  6
                      N3555(times)  =  4
               重寻呼间隔递增值(s)  =  0
            高优先级业务的T3513(s)  =  2
        高优先级业务的N3513(times)  =  4
 高优先级业务的重寻呼间隔递增值(s)  =  0
               移动可达定时器(min)  =  58
   不可达用户隐式去注册定时器(min)  =  60
                        GUTI重分配  =  初始注册&移动性注册
               GUTI重分配定时器(h)  =  0
             Handover准备定时器(s)  =  10
         源侧Handover完成定时器(s)  =  10
       目标侧Handover完成定时器(s)  =  10
                       T3定时器(s)  =  10
         测试用GUTI重分配定时器(m)  =  0
         切换流程资源释放定时器(s)  =  2
             GUTI重分配最大间隔(h)  =  0
   用户去注册后签约数据保留时间(h)  =  24
等待gNodeB上下文释放完成定时器 (s)  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGMMPARA.md`
