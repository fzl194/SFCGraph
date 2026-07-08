---
id: UNC@20.15.2@MMLCommand@LST SYSPLTPARA
type: MMLCommand
name: LST SYSPLTPARA（查询产品平台参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SYSPLTPARA
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统参数管理
status: active
---

# LST SYSPLTPARA（查询产品平台参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询产品平台相关的控制参数

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SYSPLTPARA]] · 产品平台参数（SYSPLTPARA）

## 使用实例

查询产品平台参数：

LST SYSPLTPARA:;

```
%%LST SYSPLTPARA:;%%
RETCODE = 0  操作成功

操作结果如下
--------------
        VNFC故障检测阈值（次数）  =  20
                  VNFC探测开关  =  打开
               主动关闭链路开关  =  打开
             非期望报文转发开关  =  打开
           海量SCTP消息防护开关  =  打开
   海量SCTP消息识别门限（包/秒）  =  1000
       异常eNodeB屏蔽时长（秒）  =  600
	  
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询产品平台参数(LST-SYSPLTPARA)_72345949.md`
