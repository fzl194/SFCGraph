---
id: UNC@20.15.2@MMLCommand@LST USRSECAUTH
type: MMLCommand
name: LST USRSECAUTH（查看二次授权用户）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRSECAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 二次授权用户管理
status: active
---

# LST USRSECAUTH（查看二次授权用户）

## 功能

查询所有支持二次授权的用户名。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRSECAUTH]] · 二次授权用户（USRSECAUTH）

## 使用实例

查看二次授权用户：

```
%%LST USRSECAUTH:;%%
RETCODE = 0  操作成功

操作结果如下
------------
用户名    
  
admin     
test01   
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRSECAUTH.md`
