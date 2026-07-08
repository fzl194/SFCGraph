---
id: UNC@20.15.2@MMLCommand@DSP TRCSMSGTOTALSTC
type: MMLCommand
name: DSP TRCSMSGTOTALSTC（查询跟踪中心消息统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TRCSMSGTOTALSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 跟踪管理调测
status: active
---

# DSP TRCSMSGTOTALSTC（查询跟踪中心消息统计信息）

## 功能

该命令用于查询跟踪中心消息5分钟内的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRCSMSGTOTALSTC]] · 跟踪中心消息统计信息（TRCSMSGTOTALSTC）

## 使用实例

查询跟踪中心消息统计信息，可通过如下命令查询：

```
DSP TRCSMSGTOTALSTC:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0 操作成功

结果如下:
------------------------
                    开始统计时间 = 2016-02-26T09:53:45
                    收到消息计数 = 12
                    丢弃消息计数 = 0
            任务不存在丢弃消息数 = 0
            接收缓存满丢弃消息数 = 0
   发送NETCONF缓存不存在消息计数 = 0
        订阅信息不存在丢弃消息数 = 0
      获取消息编号失败丢弃消息数 = 0
添加消息到接收缓存失败丢弃消息数 = 0
     NETCONF组件不可用丢弃消息数 = 0
添加消息到发送缓存失败丢弃消息数 = 0
            写文件失败丢弃消息数 = 0
 发送消息到NETCONF失败丢弃消息数 = 0
        发送消息缓存满丢弃消息数 = 0
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TRCSMSGTOTALSTC.md`
