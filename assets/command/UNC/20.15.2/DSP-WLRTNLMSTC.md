---
id: UNC@20.15.2@MMLCommand@DSP WLRTNLMSTC
type: MMLCommand
name: DSP WLRTNLMSTC（查询WLR组件与TNLM交互的统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRTNLMSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示隧道统计信息
status: active
---

# DSP WLRTNLMSTC（查询WLR组件与TNLM交互的统计信息）

## 功能

查询WLR组件与TNLM交互的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@WLRTNLMSTC]] · WLR组件与TNLM交互的统计信息（WLRTNLMSTC）

## 使用实例

查询WLR组件与TNLM交互的统计信息：

```
DSP WLRTNLMSTC:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
        总数  =  1
      添加数  =  1
      删除数  =  0
      更新数  =  0
序列号错误数  =  0
      对帐数  =  0
      批量数  =  1
      平滑数  =  1
    最后原因  =  对账请求
最后开始时间  =  2017-12-01 11:37:27
最后结束时间  =  2017-12-01 11:37:27
生产者状态机  =  正常
  隧道状态机  =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-WLRTNLMSTC.md`
