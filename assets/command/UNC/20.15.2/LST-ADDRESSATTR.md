---
id: UNC@20.15.2@MMLCommand@LST ADDRESSATTR
type: MMLCommand
name: LST ADDRESSATTR（查询UE IP地址属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRESSATTR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 全局地址分配属性配置
status: active
---

# LST ADDRESSATTR（查询UE IP地址属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询UE IP动态地址分配全局属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRESSATTR]] · UE IP地址属性（ADDRESSATTR）

## 使用实例

查询当前UE地址属性，可以执行如下命令：

```
%%LST ADDRESSATTR:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                              UE地址分配属性  =  SMF分配
  用户的IPv6地址Interface Identifier生成方式  =  本地
                      地址子段回收定时器(秒)  =  600
                      释放租约内地址数量(个)  =  512
                会话激活失败地址释放时长(秒)  =  5
                UPF分配地址使用情况上报开关 = FALSE
                      地址冲突时去激活策略 = DEACBOTH
AAA未下发地址池通配符的情况下是否开启通配功能 = 去使能
                         静态地址冲突检查开关 = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRESSATTR.md`
