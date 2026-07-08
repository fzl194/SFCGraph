---
id: UNC@20.15.2@MMLCommand@LST NGLANFUNC
type: MMLCommand
name: LST NGLANFUNC（查询NGLAN扩展功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGLANFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 会话管理扩展功能
status: active
---

# LST NGLANFUNC（查询NGLAN扩展功能）

## 功能

**适用NF：SMF**

该命令用于查询5G LAN特性相关的功能控制设置参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NGLAN扩展功能（NGLANFUNC）](configobject/UNC/20.15.2/NGLANFUNC.md)

## 使用实例

查询所有NGLANFUNC记录：

```
%%LST NGLANFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
      是否向UDM请求获取5G LAN组ID  =  支持
                 是否支持N19通信  =  不支持
         以太会话锚点重定位功能开关  =  不支持
              是否创建组播PDR规则  =  不支持
是否发起SMF内5G Lan组内会话数量核查  =  支持
         是否发起向UPF的组会话核查  =  支持
优选5G Lan组内已有的主锚点UPF的开关  =  不支持
             是否支持N6侧上行广播  =  不支持
             是否支持报文增殖消除  =  不支持
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NGLAN扩展功能（LST-NGLANFUNC）_98868305.md`
