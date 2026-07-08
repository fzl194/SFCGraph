---
id: UNC@20.15.2@MMLCommand@LST HTTPFCCONF
type: MMLCommand
name: LST HTTPFCCONF（查询HTTP流控属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPFCCONF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控属性管理
status: active
---

# LST HTTPFCCONF（查询HTTP流控属性）

## 功能

该命令用于查询HTTP流控属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPFCCONF]] · HTTP流控属性（HTTPFCCONF）

## 使用实例

如果想查询HTTP流控属性配置，可执行如下命令：

```
%%LST HTTPFCCONF:;%%
RETCODE = 0  操作成功

结果如下
--------
                Retry-After功能开关   =  关闭
               内存流控功能开关       =  打开
           首消息跟踪流控阈值（条/秒）=  100
             用户跟踪流控阈值（条/秒）=  300
协议消息大包跟踪流控阈值（KBytes/秒） =  1024
内部消息大包跟踪流控阈值（KBytes/秒） =  512
                大包判定阈值（Bytes） =  4096
	    接口跟踪流控阈值（条/秒） =  40
		    跟踪流控功能开关  =  打开
		 CPU跟踪流控功能开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP流控属性（LST-HTTPFCCONF）_00360893.md`
