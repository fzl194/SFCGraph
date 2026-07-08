---
id: UNC@20.15.2@MMLCommand@DSP TRCTASKSESSION
type: MMLCommand
name: DSP TRCTASKSESSION（显示跟踪任务Session信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TRCTASKSESSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 跟踪管理调测
status: active
---

# DSP TRCTASKSESSION（显示跟踪任务Session信息）

## 功能

该命令用于显示跟踪任务session信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRCTASKSESSION]] · 跟踪任务Session信息（TRCTASKSESSION）

## 使用实例

显示跟踪任务session信息：

```
DSP TRCTASKSESSION:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下
--------
            跟踪任务号  =  10
          跟踪业务类型  =  120
              上报方式  =  消息上报
生成的文件大小（字节）  =  204800
    生成文件周期（秒）  =  60
        握手周期（秒）  =  180
                  句柄  =  DK%s
      跟踪任务运行状态  =  正常
      Notification编号  =  1
           创建session  =  4294967295
           订阅session  =  NULL
                  类型  =  普通跟踪
                跟踪ID  =  4294967295
              连接句柄  =  NULL
              生成类型  =  用户生成
              服务类型  =  跟踪
            需要重定向  =  TRUE
          保留任务配置  =  TRUE
任务创建或配置恢复时间  =  2019-06-11 16:48:32
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示跟踪任务Session信息（DSP-TRCTASKSESSION）_59103685.md`
