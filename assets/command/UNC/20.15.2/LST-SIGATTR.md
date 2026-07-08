---
id: UNC@20.15.2@MMLCommand@LST SIGATTR
type: MMLCommand
name: LST SIGATTR（查询信令网属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SIGATTR
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- 信令网属性管理
status: active
---

# LST SIGATTR（查询信令网属性）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询信令网属性配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SIGATTR]] · 信令网属性状态（SIGATTR）

## 使用实例

查询已经设置的信令网属性：

```
LST SIGATTR:;
```

```
%%LST SIGATTR:;%%
RETCODE = 0  操作成功。

信令网属性表
------------
       国际网标志  =  14位
   国际备用网标志  =  14位
       国内网标志  =  24位
   国内备用网标志  =  24位
     M3UA STP功能  =  否    
   是否支持BSSAP+  =  是
   BSSAP+子系统号  =  252
 BSSAP+所在信令网  =  国内网
    MAP所在信令网  =  国内网
   信令网协议类型  =  ITUT_SS7
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SIGATTR.md`
