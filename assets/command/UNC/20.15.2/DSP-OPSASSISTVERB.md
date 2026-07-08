---
id: UNC@20.15.2@MMLCommand@DSP OPSASSISTVERB
type: MMLCommand
name: DSP OPSASSISTVERB（显示系统助手的详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OPSASSISTVERB
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 开放可编程系统
status: active
---

# DSP OPSASSISTVERB（显示系统助手的详细信息）

## 功能

该命令用于显示系统助手的详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OPSASSISTVERB]] · 系统助手的详细信息（OPSASSISTVERB）

## 使用实例

显示系统助手的详细信息：

```
DSP OPSASSISTVERB:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                                助手ID  =  2
                              助手名称  =  _get_all_env.py
                              助手状态  =  准备好状态
                              助手类型  =  脚本
                      是否默认维护助手  =  TRUE
                              运行次数  =  824
                  维护助手缓存最大个数  =  100
                  当前维护助手可用个数  =  100
                    因队列满丢弃的任务  =  9226
                  延迟期间丢弃的任务数  =  0
                    被抑制的触发总次数  =  0
              因为错误而丢弃的触发次数  =  0
                              助手摘要  =  _get_all_env.py : ops_execute()
        多条件组合周期内发生次数的阈值  =  1
              多条件组合检查周期（秒）  =  30
多条件组合触发工作任务的延迟时间（秒）  =  0
                    周期内最大触发次数  =  0
                    多条件组合命中次数  =  0
                          条件组合方式  =  NULL
                          条件标签名称  =  NULL
                          触发条件类型  =  事件
                              订阅状态  =  0
              条件周期内发生次数的阈值  =  1
                    条件检查周期（秒）  =  30
            条件组合条件周期内命中次数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OPSASSISTVERB.md`
