---
id: UNC@20.15.2@MMLCommand@LST T1N1PARA
type: MMLCommand
name: LST T1N1PARA（查询PFCP T1N1参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: T1N1PARA
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP消息可靠性管理
status: active
---

# LST T1N1PARA（查询PFCP T1N1参数配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询消息的超时间隔和发送次数阈值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@T1N1PARA]] · PFCP T1N1参数配置（T1N1PARA）

## 使用实例

查询所有消息的超时间隔和发送次数阈值。 LST T1N1PARA:;

```
%%LST T1N1PARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
发送次数阈值  超时间隔(秒)  消息类型
    
3             10            偶联建立消息      
2             3             偶联更新消息      
2             3             偶联释放消息   
2             3             会话建立消息
2             3             会话更新消息   
2             3             会话删除消息 
(结果个数 = 6)

---      END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-T1N1PARA.md`
